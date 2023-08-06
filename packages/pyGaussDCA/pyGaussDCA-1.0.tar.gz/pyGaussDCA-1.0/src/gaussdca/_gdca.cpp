#include <pythonic/core.hpp>
#include <pythonic/python/core.hpp>
#include <pythonic/types/bool.hpp>
#include <pythonic/types/int.hpp>
#ifdef _OPENMP
#include <omp.h>
#endif
#include <pythonic/include/types/int8.hpp>
#include <pythonic/include/types/float64.hpp>
#include <pythonic/include/types/ndarray.hpp>
#include <pythonic/include/types/int.hpp>
#include <pythonic/include/types/float.hpp>
#include <pythonic/include/types/numpy_texpr.hpp>
#include <pythonic/types/float64.hpp>
#include <pythonic/types/int.hpp>
#include <pythonic/types/int8.hpp>
#include <pythonic/types/float.hpp>
#include <pythonic/types/ndarray.hpp>
#include <pythonic/types/numpy_texpr.hpp>
#include <pythonic/include/__builtin__/None.hpp>
#include <pythonic/include/__builtin__/getattr.hpp>
#include <pythonic/include/__builtin__/min.hpp>
#include <pythonic/include/__builtin__/pythran/and_.hpp>
#include <pythonic/include/__builtin__/pythran/make_shape.hpp>
#include <pythonic/include/__builtin__/range.hpp>
#include <pythonic/include/__builtin__/tuple.hpp>
#include <pythonic/include/numpy/bincount.hpp>
#include <pythonic/include/numpy/fill_diagonal.hpp>
#include <pythonic/include/numpy/float64.hpp>
#include <pythonic/include/numpy/floor.hpp>
#include <pythonic/include/numpy/max.hpp>
#include <pythonic/include/numpy/maximum.hpp>
#include <pythonic/include/numpy/mean.hpp>
#include <pythonic/include/numpy/ones.hpp>
#include <pythonic/include/numpy/sqrt.hpp>
#include <pythonic/include/numpy/square.hpp>
#include <pythonic/include/numpy/sum.hpp>
#include <pythonic/include/numpy/zeros.hpp>
#include <pythonic/include/operator_/add.hpp>
#include <pythonic/include/operator_/div.hpp>
#include <pythonic/include/operator_/eq.hpp>
#include <pythonic/include/operator_/idiv.hpp>
#include <pythonic/include/operator_/le.hpp>
#include <pythonic/include/operator_/lt.hpp>
#include <pythonic/include/operator_/mul.hpp>
#include <pythonic/include/operator_/ne.hpp>
#include <pythonic/include/types/slice.hpp>
#include <pythonic/include/types/str.hpp>
#include <pythonic/__builtin__/None.hpp>
#include <pythonic/__builtin__/getattr.hpp>
#include <pythonic/__builtin__/min.hpp>
#include <pythonic/__builtin__/pythran/and_.hpp>
#include <pythonic/__builtin__/pythran/make_shape.hpp>
#include <pythonic/__builtin__/range.hpp>
#include <pythonic/__builtin__/tuple.hpp>
#include <pythonic/numpy/bincount.hpp>
#include <pythonic/numpy/fill_diagonal.hpp>
#include <pythonic/numpy/float64.hpp>
#include <pythonic/numpy/floor.hpp>
#include <pythonic/numpy/max.hpp>
#include <pythonic/numpy/maximum.hpp>
#include <pythonic/numpy/mean.hpp>
#include <pythonic/numpy/ones.hpp>
#include <pythonic/numpy/sqrt.hpp>
#include <pythonic/numpy/square.hpp>
#include <pythonic/numpy/sum.hpp>
#include <pythonic/numpy/zeros.hpp>
#include <pythonic/operator_/add.hpp>
#include <pythonic/operator_/div.hpp>
#include <pythonic/operator_/eq.hpp>
#include <pythonic/operator_/idiv.hpp>
#include <pythonic/operator_/le.hpp>
#include <pythonic/operator_/lt.hpp>
#include <pythonic/operator_/mul.hpp>
#include <pythonic/operator_/ne.hpp>
#include <pythonic/types/slice.hpp>
#include <pythonic/types/str.hpp>
namespace __pythran__gdca
{
  struct _add_pseudocount
  {
    typedef void callable;
    typedef void pure;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 >
    struct type
    {
      typedef long __type0;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type1;
      typedef decltype((std::declval<__type0>() - std::declval<__type1>())) __type2;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type3;
      typedef decltype((pythonic::operator_::mul(std::declval<__type2>(), std::declval<__type3>()))) __type4;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type4>::type>::type __type5;
      typedef typename pythonic::assignable<decltype((pythonic::operator_::div(std::declval<__type1>(), std::declval<__type5>())))>::type __type6;
      typedef decltype((pythonic::operator_::add(std::declval<__type4>(), std::declval<__type6>()))) __type7;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type8;
      typedef decltype((pythonic::operator_::mul(std::declval<__type2>(), std::declval<__type8>()))) __type9;
      typedef decltype((pythonic::operator_::div(std::declval<__type6>(), std::declval<__type5>()))) __type10;
      typedef typename pythonic::assignable<decltype((pythonic::operator_::add(std::declval<__type9>(), std::declval<__type10>())))>::type __type11;
      typedef typename pythonic::assignable<long>::type __type12;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::range{})>::type>::type __type13;
      typedef typename pythonic::assignable<decltype((std::declval<__type5>() - std::declval<__type0>()))>::type __type14;
      typedef decltype(std::declval<__type13>()(std::declval<__type14>())) __type15;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type15>::type::iterator>::value_type>::type __type16;
      typedef typename pythonic::assignable<decltype((pythonic::operator_::add(std::declval<__type12>(), std::declval<__type16>())))>::type __type17;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type17>(), std::declval<__type17>())) __type18;
      typedef indexable<__type18> __type19;
      typedef typename __combined<__type11,__type19>::type __type20;
      typedef pythonic::types::contiguous_slice __type21;
      typedef decltype(std::declval<__type8>()(std::declval<__type21>(), std::declval<__type21>())) __type22;
      typedef decltype((pythonic::operator_::mul(std::declval<__type2>(), std::declval<__type22>()))) __type23;
      typedef container<typename std::remove_reference<__type23>::type> __type24;
      typedef typename __combined<__type20,__type24>::type __type25;
      typedef typename __combined<__type25,__type19>::type __type26;
      typedef container<typename std::remove_reference<__type6>::type> __type27;
      typedef typename __combined<__type26,__type27>::type __type28;
      typedef typename pythonic::returnable<decltype(pythonic::types::make_tuple(std::declval<__type7>(), std::declval<__type28>()))>::type result_type;
    }  
    ;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 >
    typename type<argument_type0, argument_type1, argument_type2, argument_type3, argument_type4>::result_type operator()(argument_type0&& Pi_true, argument_type1&& Pij_true, argument_type2&& pc, argument_type3&& n_cols, argument_type4&& q) const
    ;
  }  ;
  struct _compute_freqs
  {
    typedef void callable;
    typedef void pure;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 >
    struct type
    {
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::zeros{})>::type>::type __type0;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type1;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type3>::type>::type __type2;
      typedef long __type3;
      typedef typename pythonic::assignable<decltype((std::declval<__type2>() - std::declval<__type3>()))>::type __type4;
      typedef typename pythonic::assignable<decltype((pythonic::operator_::mul(std::declval<__type1>(), std::declval<__type4>())))>::type __type5;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::float64{})>::type>::type __type6;
      typedef typename pythonic::assignable<decltype(std::declval<__type0>()(std::declval<__type5>(), std::declval<__type6>()))>::type __type7;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::range{})>::type>::type __type8;
      typedef decltype(std::declval<__type8>()(std::declval<__type1>())) __type9;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type9>::type::iterator>::value_type>::type __type10;
      typedef decltype((pythonic::operator_::mul(std::declval<__type10>(), std::declval<__type4>()))) __type11;
      typedef typename pythonic::lazy<__type11>::type __type12;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type13;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type14;
      typedef decltype(std::declval<__type8>()(std::declval<__type14>())) __type15;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type15>::type::iterator>::value_type>::type __type16;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type10>(), std::declval<__type16>())) __type17;
      typedef decltype(std::declval<__type13>()[std::declval<__type17>()]) __type18;
      typedef decltype((pythonic::operator_::add(std::declval<__type12>(), std::declval<__type18>()))) __type19;
      typedef decltype((std::declval<__type19>() - std::declval<__type3>())) __type20;
      typedef indexable<__type20> __type21;
      typedef typename __combined<__type7,__type21>::type __type22;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::sum{})>::type>::type __type23;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type4>::type>::type __type24;
      typedef typename pythonic::assignable<decltype(std::declval<__type23>()(std::declval<__type24>()))>::type __type25;
      typedef decltype((pythonic::operator_::div(std::declval<__type22>(), std::declval<__type25>()))) __type26;
      typedef typename __combined<__type22,__type26>::type __type27;
      typedef typename __combined<__type27,__type21>::type __type28;
      typedef decltype(std::declval<__type24>()[std::declval<__type16>()]) __type29;
      typedef container<typename std::remove_reference<__type29>::type> __type30;
      typedef typename __combined<__type28,__type30>::type __type31;
      typedef typename __combined<__type31,__type25>::type __type32;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::maximum{})>::type>::type __type33;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::pythran::functor::make_shape{})>::type>::type __type34;
      typedef decltype(std::declval<__type34>()(std::declval<__type5>(), std::declval<__type5>())) __type35;
      typedef typename pythonic::assignable<decltype(std::declval<__type0>()(std::declval<__type35>(), std::declval<__type6>()))>::type __type36;
      typedef decltype((pythonic::operator_::mul(std::declval<__type11>(), std::declval<__type10>()))) __type37;
      typedef decltype((pythonic::operator_::mul(std::declval<__type37>(), std::declval<__type4>()))) __type38;
      typedef decltype((pythonic::operator_::add(std::declval<__type38>(), std::declval<__type18>()))) __type39;
      typedef decltype((std::declval<__type39>() - std::declval<__type3>())) __type40;
      typedef decltype(std::declval<__type8>()(std::declval<__type10>(), std::declval<__type1>())) __type41;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type41>::type::iterator>::value_type>::type __type42;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type42>(), std::declval<__type16>())) __type43;
      typedef decltype(std::declval<__type13>()[std::declval<__type43>()]) __type44;
      typedef decltype((pythonic::operator_::add(std::declval<__type12>(), std::declval<__type44>()))) __type45;
      typedef decltype((std::declval<__type45>() - std::declval<__type3>())) __type46;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type40>(), std::declval<__type46>())) __type47;
      typedef indexable<__type47> __type48;
      typedef typename __combined<__type36,__type48>::type __type49;
      typedef typename __combined<__type49,__type30>::type __type50;
      typedef decltype(pythonic::__builtin__::getattr(pythonic::types::attr::T{}, std::declval<__type50>())) __type51;
      typedef typename pythonic::assignable<decltype(std::declval<__type33>()(std::declval<__type50>(), std::declval<__type51>()))>::type __type52;
      typedef decltype((pythonic::operator_::div(std::declval<__type52>(), std::declval<__type25>()))) __type53;
      typedef typename __combined<__type52,__type53>::type __type54;
      typedef typename __combined<__type54,__type25>::type __type55;
      typedef typename pythonic::returnable<decltype(pythonic::types::make_tuple(std::declval<__type32>(), std::declval<__type55>()))>::type result_type;
    }  
    ;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 >
    typename type<argument_type0, argument_type1, argument_type2, argument_type3, argument_type4>::result_type operator()(argument_type0&& alignment, argument_type1&& n_cols, argument_type2&& depth, argument_type3&& q, argument_type4&& W) const
    ;
  }  ;
  struct _compute_weights
  {
    typedef void callable;
    typedef void pure;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 >
    struct type
    {
      typedef typename std::remove_cv<typename std::remove_reference<argument_type3>::type>::type __type0;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::ones{})>::type>::type __type1;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::float64{})>::type>::type __type2;
      typedef typename pythonic::assignable<decltype(std::declval<__type1>()(std::declval<__type0>(), std::declval<__type2>()))>::type __type3;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type0>(), std::declval<__type3>())) __type4;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::sum{})>::type>::type __type5;
      typedef double __type6;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::range{})>::type>::type __type7;
      typedef long __type8;
      typedef decltype((std::declval<__type0>() - std::declval<__type8>())) __type9;
      typedef decltype(std::declval<__type7>()(std::declval<__type9>())) __type10;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type10>::type::iterator>::value_type>::type __type11;
      typedef indexable<__type11> __type12;
      typedef typename __combined<__type3,__type12>::type __type13;
      typedef decltype((pythonic::operator_::add(std::declval<__type11>(), std::declval<__type8>()))) __type14;
      typedef decltype(std::declval<__type7>()(std::declval<__type14>(), std::declval<__type0>())) __type15;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type15>::type::iterator>::value_type>::type __type16;
      typedef indexable<__type16> __type17;
      typedef typename __combined<__type13,__type17>::type __type18;
      typedef typename __combined<__type18,__type12>::type __type19;
      typedef container<typename std::remove_reference<__type6>::type> __type20;
      typedef typename __combined<__type19,__type20>::type __type21;
      typedef typename __combined<__type21,__type17>::type __type22;
      typedef typename __combined<__type22,__type20>::type __type23;
      typedef typename pythonic::assignable<decltype((pythonic::operator_::div(std::declval<__type6>(), std::declval<__type23>())))>::type __type24;
      typedef decltype(std::declval<__type5>()(std::declval<__type24>())) __type25;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type25>(), std::declval<__type24>())) __type26;
      typedef typename pythonic::returnable<typename __combined<__type4,__type26>::type>::type result_type;
    }  
    ;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 >
    typename type<argument_type0, argument_type1, argument_type2, argument_type3>::result_type operator()(argument_type0&& alignment, argument_type1&& theta, argument_type2&& n_cols, argument_type3&& depth) const
    ;
  }  ;
  struct _compute_theta
  {
    typedef void callable;
    typedef void pure;
    template <typename argument_type0 >
    struct type
    {
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::min{})>::type>::type __type0;
      typedef double __type1;
      typedef typename pythonic::assignable<double>::type __type2;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::sum{})>::type>::type __type3;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::bincount{})>::type>::type __type4;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type5;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::range{})>::type>::type __type6;
      typedef decltype(pythonic::__builtin__::getattr(pythonic::types::attr::SHAPE{}, std::declval<__type5>())) __type7;
      typedef typename std::tuple_element<0,typename std::remove_reference<__type7>::type>::type __type8;
      typedef decltype(std::declval<__type6>()(std::declval<__type8>())) __type9;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type9>::type::iterator>::value_type>::type __type10;
      typedef pythonic::types::contiguous_slice __type11;
      typedef decltype(std::declval<__type5>()(std::declval<__type10>(), std::declval<__type11>())) __type12;
      typedef typename pythonic::assignable<decltype(std::declval<__type4>()(std::declval<__type12>()))>::type __type13;
      typedef long __type14;
      typedef decltype((std::declval<__type13>() - std::declval<__type14>())) __type15;
      typedef decltype((pythonic::operator_::mul(std::declval<__type13>(), std::declval<__type15>()))) __type16;
      typedef decltype((pythonic::operator_::div(std::declval<__type16>(), std::declval<__type14>()))) __type17;
      typedef decltype(std::declval<__type3>()(std::declval<__type17>())) __type18;
      typedef decltype((pythonic::operator_::add(std::declval<__type2>(), std::declval<__type18>()))) __type19;
      typedef typename __combined<__type2,__type19>::type __type20;
      typedef typename pythonic::assignable<typename std::tuple_element<1,typename std::remove_reference<__type7>::type>::type>::type __type21;
      typedef decltype((pythonic::operator_::mul(std::declval<__type1>(), std::declval<__type21>()))) __type22;
      typedef decltype((std::declval<__type21>() - std::declval<__type14>())) __type23;
      typedef decltype((pythonic::operator_::mul(std::declval<__type22>(), std::declval<__type23>()))) __type24;
      typedef decltype((pythonic::operator_::mul(std::declval<__type24>(), std::declval<__type8>()))) __type25;
      typedef decltype((pythonic::operator_::div(std::declval<__type20>(), std::declval<__type25>()))) __type26;
      typedef typename __combined<__type20,__type26>::type __type27;
      typedef typename __combined<__type27,__type18>::type __type28;
      typedef typename __combined<__type28,__type25>::type __type29;
      typedef decltype((pythonic::operator_::div(std::declval<__type1>(), std::declval<__type29>()))) __type30;
      typedef typename pythonic::returnable<decltype(std::declval<__type0>()(std::declval<__type1>(), std::declval<__type30>()))>::type result_type;
    }  
    ;
    template <typename argument_type0 >
    typename type<argument_type0>::result_type operator()(argument_type0&& alignment) const
    ;
  }  ;
  struct apc_correction
  {
    typedef void callable;
    typedef void pure;
    template <typename argument_type0 >
    struct type
    {
      typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type0;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::mean{})>::type>::type __type1;
      typedef long __type2;
      typedef decltype(std::declval<__type1>()(std::declval<__type0>(), std::declval<__type2>())) __type3;
      typedef pythonic::types::none_type __type4;
      typedef pythonic::types::contiguous_slice __type5;
      typedef decltype(std::declval<__type3>()(std::declval<__type4>(), std::declval<__type5>())) __type6;
      typedef decltype(std::declval<__type3>()(std::declval<__type5>(), std::declval<__type4>())) __type7;
      typedef decltype((pythonic::operator_::mul(std::declval<__type6>(), std::declval<__type7>()))) __type8;
      typedef decltype(std::declval<__type1>()(std::declval<__type0>())) __type9;
      typedef decltype((pythonic::operator_::div(std::declval<__type8>(), std::declval<__type9>()))) __type10;
      typedef typename pythonic::returnable<typename pythonic::assignable<decltype((std::declval<__type0>() - std::declval<__type10>()))>::type>::type result_type;
    }  
    ;
    template <typename argument_type0 >
    typename type<argument_type0>::result_type operator()(argument_type0&& matrix) const
    ;
  }  ;
  struct compute_FN
  {
    typedef void callable;
    typedef void pure;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 >
    struct type
    {
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::sqrt{})>::type>::type __type0;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::zeros{})>::type>::type __type1;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::pythran::functor::make_shape{})>::type>::type __type2;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type3;
      typedef decltype(std::declval<__type2>()(std::declval<__type3>(), std::declval<__type3>())) __type4;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::float64{})>::type>::type __type5;
      typedef typename pythonic::assignable<decltype(std::declval<__type1>()(std::declval<__type4>(), std::declval<__type5>()))>::type __type6;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::range{})>::type>::type __type7;
      typedef long __type8;
      typedef decltype((std::declval<__type3>() - std::declval<__type8>())) __type9;
      typedef decltype(std::declval<__type7>()(std::declval<__type9>())) __type10;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type10>::type::iterator>::value_type>::type __type11;
      typedef decltype((pythonic::operator_::add(std::declval<__type11>(), std::declval<__type8>()))) __type12;
      typedef decltype(std::declval<__type7>()(std::declval<__type12>(), std::declval<__type3>())) __type13;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type13>::type::iterator>::value_type>::type __type14;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type11>(), std::declval<__type14>())) __type15;
      typedef indexable<__type15> __type16;
      typedef typename __combined<__type6,__type16>::type __type17;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type14>(), std::declval<__type11>())) __type18;
      typedef indexable<__type18> __type19;
      typedef typename __combined<__type17,__type19>::type __type20;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::sum{})>::type>::type __type21;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::square{})>::type>::type __type22;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type23;
      typedef pythonic::types::contiguous_slice __type24;
      typedef typename pythonic::assignable<decltype(std::declval<__type23>()(std::declval<__type24>(), std::declval<__type24>()))>::type __type25;
      typedef decltype(std::declval<__type21>()(std::declval<__type25>(), std::declval<__type8>())) __type26;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type27;
      typedef typename pythonic::assignable<typename pythonic::assignable<decltype((std::declval<__type27>() - std::declval<__type8>()))>::type>::type __type28;
      typedef decltype((pythonic::operator_::div(std::declval<__type26>(), std::declval<__type28>()))) __type29;
      typedef pythonic::types::none_type __type30;
      typedef decltype(std::declval<__type29>()(std::declval<__type24>(), std::declval<__type30>())) __type31;
      typedef decltype((std::declval<__type25>() - std::declval<__type31>())) __type32;
      typedef decltype(std::declval<__type29>()(std::declval<__type30>(), std::declval<__type24>())) __type33;
      typedef decltype((std::declval<__type32>() - std::declval<__type33>())) __type34;
      typedef decltype(std::declval<__type21>()(std::declval<__type25>())) __type35;
      typedef typename pythonic::assignable<decltype((std::declval<__type27>() - std::declval<__type8>()))>::type __type36;
      typedef typename pythonic::assignable<decltype(std::declval<__type22>()(std::declval<__type36>()))>::type __type37;
      typedef decltype((pythonic::operator_::div(std::declval<__type35>(), std::declval<__type37>()))) __type38;
      typedef decltype((pythonic::operator_::add(std::declval<__type34>(), std::declval<__type38>()))) __type39;
      typedef decltype(std::declval<__type22>()(std::declval<__type39>())) __type40;
      typedef typename pythonic::assignable<decltype(std::declval<__type21>()(std::declval<__type40>()))>::type __type41;
      typedef container<typename std::remove_reference<__type41>::type> __type42;
      typedef typename __combined<__type20,__type42>::type __type43;
      typedef typename __combined<__type43,__type16>::type __type44;
      typedef typename __combined<__type44,__type42>::type __type45;
      typedef typename __combined<__type45,__type19>::type __type46;
      typedef typename __combined<__type46,__type42>::type __type47;
      typedef typename pythonic::assignable<decltype(std::declval<__type0>()(std::declval<__type47>()))>::type __type48;
      typedef apc_correction __type49;
      typedef decltype(std::declval<__type49>()(std::declval<__type48>())) __type50;
      typedef typename pythonic::returnable<decltype(pythonic::types::make_tuple(std::declval<__type48>(), std::declval<__type50>()))>::type result_type;
    }  
    ;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 >
    typename type<argument_type0, argument_type1, argument_type2>::result_type operator()(argument_type0&& mJ, argument_type1&& n_cols, argument_type2&& alphabet_size) const
    ;
  }  ;
  struct compute_weights
  {
    typedef void callable;
    typedef void pure;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 >
    struct type
    {
      typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type0;
      typedef _compute_weights __type1;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type2;
      typedef typename pythonic::assignable<typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type>::type __type3;
      typedef _compute_theta __type4;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type5;
      typedef typename pythonic::assignable<decltype(std::declval<__type4>()(std::declval<__type5>()))>::type __type6;
      typedef typename __combined<__type3,__type6>::type __type7;
      typedef decltype(pythonic::__builtin__::getattr(pythonic::types::attr::SHAPE{}, std::declval<__type2>())) __type8;
      typedef typename std::tuple_element<1,typename std::remove_reference<__type8>::type>::type __type9;
      typedef typename std::tuple_element<0,typename std::remove_reference<__type8>::type>::type __type10;
      typedef decltype(std::declval<__type1>()(std::declval<__type2>(), std::declval<__type7>(), std::declval<__type9>(), std::declval<__type10>())) __type11;
      typedef __type0 __ptype0;
      typedef typename pythonic::returnable<typename std::tuple_element<1,typename std::remove_reference<__type11>::type>::type>::type result_type;
    }  
    ;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 >
    typename type<argument_type0, argument_type1, argument_type2>::result_type operator()(argument_type0&& alignment, argument_type1&& alignment_T, argument_type2&& theta) const
    ;
  }  ;
  struct _compute_covar
  {
    typedef void callable;
    typedef void pure;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 >
    struct type
    {
      typedef _add_pseudocount __type0;
      typedef _compute_freqs __type1;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type2;
      typedef decltype(pythonic::__builtin__::getattr(pythonic::types::attr::SHAPE{}, std::declval<__type2>())) __type3;
      typedef typename pythonic::assignable<typename std::tuple_element<0,typename std::remove_reference<__type3>::type>::type>::type __type4;
      typedef typename std::tuple_element<1,typename std::remove_reference<__type3>::type>::type __type5;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::max{})>::type>::type __type6;
      typedef typename pythonic::assignable<decltype(std::declval<__type6>()(std::declval<__type2>()))>::type __type7;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type8;
      typedef typename pythonic::assignable<decltype(std::declval<__type1>()(std::declval<__type2>(), std::declval<__type4>(), std::declval<__type5>(), std::declval<__type7>(), std::declval<__type8>()))>::type __type9;
      typedef typename std::tuple_element<0,typename std::remove_reference<__type9>::type>::type __type10;
      typedef typename std::tuple_element<1,typename std::remove_reference<__type9>::type>::type __type11;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type12;
      typedef typename pythonic::assignable<decltype(std::declval<__type0>()(std::declval<__type10>(), std::declval<__type11>(), std::declval<__type12>(), std::declval<__type4>(), std::declval<__type7>()))>::type __type13;
      typedef typename std::tuple_element<1,typename std::remove_reference<__type13>::type>::type __type14;
      typedef typename std::tuple_element<0,typename std::remove_reference<__type13>::type>::type __type15;
      typedef pythonic::types::contiguous_slice __type16;
      typedef pythonic::types::none_type __type17;
      typedef typename pythonic::assignable<decltype(std::declval<__type15>()(std::declval<__type16>(), std::declval<__type17>()))>::type __type18;
      typedef decltype(pythonic::__builtin__::getattr(pythonic::types::attr::T{}, std::declval<__type18>())) __type19;
      typedef decltype((pythonic::operator_::mul(std::declval<__type18>(), std::declval<__type19>()))) __type20;
      typedef typename pythonic::returnable<decltype((std::declval<__type14>() - std::declval<__type20>()))>::type result_type;
    }  
    ;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 >
    typename type<argument_type0, argument_type1, argument_type2>::result_type operator()(argument_type0&& alignment, argument_type1&& weights, argument_type2&& pseudocount) const
    ;
  }  ;
  struct prepare_covariance
  {
    typedef void callable;
    typedef void pure;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 = double>
    struct type
    {
      typedef _compute_covar __type0;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type1;
      typedef _compute_weights __type2;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type3;
      typedef _compute_theta __type4;
      typedef decltype(std::declval<__type4>()(std::declval<__type1>())) __type5;
      typedef decltype(pythonic::__builtin__::getattr(pythonic::types::attr::SHAPE{}, std::declval<__type3>())) __type6;
      typedef typename std::tuple_element<1,typename std::remove_reference<__type6>::type>::type __type7;
      typedef typename std::tuple_element<0,typename std::remove_reference<__type6>::type>::type __type8;
      typedef typename pythonic::assignable<decltype(std::declval<__type2>()(std::declval<__type3>(), std::declval<__type5>(), std::declval<__type7>(), std::declval<__type8>()))>::type __type9;
      typedef typename std::tuple_element<1,typename std::remove_reference<__type9>::type>::type __type10;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type11;
      typedef decltype(std::declval<__type0>()(std::declval<__type1>(), std::declval<__type10>(), std::declval<__type11>())) __type12;
      typedef typename std::tuple_element<0,typename std::remove_reference<__type9>::type>::type __type13;
      typedef typename pythonic::returnable<decltype(pythonic::types::make_tuple(std::declval<__type12>(), std::declval<__type13>()))>::type result_type;
    }  
    ;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 = double>
    typename type<argument_type0, argument_type1, argument_type2>::result_type operator()(argument_type0&& alignment, argument_type1&& alignment_T, argument_type2 pseudocount= 0.8) const
    ;
  }  ;
  template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 >
  typename _add_pseudocount::type<argument_type0, argument_type1, argument_type2, argument_type3, argument_type4>::result_type _add_pseudocount::operator()(argument_type0&& Pi_true, argument_type1&& Pij_true, argument_type2&& pc, argument_type3&& n_cols, argument_type4&& q) const
  {
    typedef long __type0;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type1;
    typedef decltype((std::declval<__type0>() - std::declval<__type1>())) __type2;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type3;
    typedef decltype((pythonic::operator_::mul(std::declval<__type2>(), std::declval<__type3>()))) __type4;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type4>::type>::type __type5;
    typedef typename pythonic::assignable<decltype((pythonic::operator_::div(std::declval<__type1>(), std::declval<__type5>())))>::type __type6;
    typedef decltype((pythonic::operator_::div(std::declval<__type6>(), std::declval<__type5>()))) __type7;
    typedef typename pythonic::assignable<decltype((pythonic::operator_::add(std::declval<__type4>(), std::declval<__type7>())))>::type __type8;
    typedef typename pythonic::assignable<long>::type __type9;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::range{})>::type>::type __type10;
    typedef typename pythonic::assignable<decltype((std::declval<__type5>() - std::declval<__type0>()))>::type __type11;
    typedef decltype(std::declval<__type10>()(std::declval<__type11>())) __type12;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type12>::type::iterator>::value_type>::type __type13;
    typedef typename pythonic::assignable<decltype((pythonic::operator_::add(std::declval<__type9>(), std::declval<__type13>())))>::type __type14;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type14>(), std::declval<__type14>())) __type15;
    typedef indexable<__type15> __type16;
    typedef typename __combined<__type8,__type16>::type __type17;
    typedef pythonic::types::contiguous_slice __type18;
    typedef decltype(std::declval<__type3>()(std::declval<__type18>(), std::declval<__type18>())) __type19;
    typedef decltype((pythonic::operator_::mul(std::declval<__type2>(), std::declval<__type19>()))) __type20;
    typedef container<typename std::remove_reference<__type20>::type> __type21;
    typedef typename __combined<__type17,__type21>::type __type22;
    typedef typename __combined<__type22,__type16>::type __type23;
    typedef container<typename std::remove_reference<__type6>::type> __type24;
    typedef decltype((pythonic::operator_::add(std::declval<__type9>(), std::declval<__type11>()))) __type25;
    typedef typename __combined<__type9,__type25>::type __type26;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type3>::type>::type __type27;
    typedef decltype(std::declval<__type10>()(std::declval<__type27>())) __type28;
    typename pythonic::assignable<typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type28>::type::iterator>::value_type>::type>::type i;
    typename pythonic::assignable<typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type12>::type::iterator>::value_type>::type>::type alpha;
    typename pythonic::assignable<decltype((pythonic::operator_::div(pc, q)))>::type pcq = (pythonic::operator_::div(pc, q));
    typename pythonic::assignable<decltype((q - 1L))>::type s = (q - 1L);
    ;
    typename pythonic::assignable<typename __combined<__type23,__type24>::type>::type Pij = (pythonic::operator_::add((pythonic::operator_::mul((1L - pc), Pij_true)), (pythonic::operator_::div(pcq, q))));
    typename pythonic::assignable<typename __combined<__type26,__type11>::type>::type i0 = 0L;
    {
      for (long  i=0L; i < n_cols; i += 1L)
      {
        Pij(pythonic::types::contiguous_slice(i0,(pythonic::operator_::add(i0, s))),pythonic::types::contiguous_slice(i0,(pythonic::operator_::add(i0, s)))) = (pythonic::operator_::mul((1L - pc), Pij_true(pythonic::types::contiguous_slice(i0,(pythonic::operator_::add(i0, s))),pythonic::types::contiguous_slice(i0,(pythonic::operator_::add(i0, s))))));
        {
          for (long  alpha=0L; alpha < s; alpha += 1L)
          {
            typename pythonic::assignable<decltype((pythonic::operator_::add(i0, alpha)))>::type x = (pythonic::operator_::add(i0, alpha));
            Pij[pythonic::types::make_tuple(x, x)] += pcq;
          }
        }
        i0 += s;
      }
    }
    return pythonic::types::make_tuple((pythonic::operator_::add((pythonic::operator_::mul((1L - pc), Pi_true)), pcq)), Pij);
  }
  template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 , typename argument_type4 >
  typename _compute_freqs::type<argument_type0, argument_type1, argument_type2, argument_type3, argument_type4>::result_type _compute_freqs::operator()(argument_type0&& alignment, argument_type1&& n_cols, argument_type2&& depth, argument_type3&& q, argument_type4&& W) const
  {
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::zeros{})>::type>::type __type0;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type1;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type3>::type>::type __type2;
    typedef long __type3;
    typedef typename pythonic::assignable<decltype((std::declval<__type2>() - std::declval<__type3>()))>::type __type4;
    typedef typename pythonic::assignable<decltype((pythonic::operator_::mul(std::declval<__type1>(), std::declval<__type4>())))>::type __type5;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::float64{})>::type>::type __type6;
    typedef typename pythonic::assignable<decltype(std::declval<__type0>()(std::declval<__type5>(), std::declval<__type6>()))>::type __type7;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::range{})>::type>::type __type8;
    typedef decltype(std::declval<__type8>()(std::declval<__type1>())) __type9;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type9>::type::iterator>::value_type>::type __type10;
    typedef decltype((pythonic::operator_::mul(std::declval<__type10>(), std::declval<__type4>()))) __type11;
    typedef typename pythonic::lazy<__type11>::type __type12;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type13;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type14;
    typedef decltype(std::declval<__type8>()(std::declval<__type14>())) __type15;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type15>::type::iterator>::value_type>::type __type16;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type10>(), std::declval<__type16>())) __type17;
    typedef decltype(std::declval<__type13>()[std::declval<__type17>()]) __type18;
    typedef decltype((pythonic::operator_::add(std::declval<__type12>(), std::declval<__type18>()))) __type19;
    typedef decltype((std::declval<__type19>() - std::declval<__type3>())) __type20;
    typedef indexable<__type20> __type21;
    typedef typename __combined<__type7,__type21>::type __type22;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::sum{})>::type>::type __type23;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type4>::type>::type __type24;
    typedef typename pythonic::assignable<decltype(std::declval<__type23>()(std::declval<__type24>()))>::type __type25;
    typedef decltype((pythonic::operator_::div(std::declval<__type22>(), std::declval<__type25>()))) __type26;
    typedef typename __combined<__type22,__type26>::type __type27;
    typedef typename __combined<__type27,__type21>::type __type28;
    typedef decltype(std::declval<__type24>()[std::declval<__type16>()]) __type29;
    typedef container<typename std::remove_reference<__type29>::type> __type30;
    typedef typename __combined<__type28,__type30>::type __type31;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::pythran::functor::make_shape{})>::type>::type __type32;
    typedef decltype(std::declval<__type32>()(std::declval<__type5>(), std::declval<__type5>())) __type33;
    typedef typename pythonic::assignable<decltype(std::declval<__type0>()(std::declval<__type33>(), std::declval<__type6>()))>::type __type34;
    typedef decltype((pythonic::operator_::mul(std::declval<__type11>(), std::declval<__type10>()))) __type35;
    typedef decltype((pythonic::operator_::mul(std::declval<__type35>(), std::declval<__type4>()))) __type36;
    typedef decltype((pythonic::operator_::add(std::declval<__type36>(), std::declval<__type18>()))) __type37;
    typedef decltype((std::declval<__type37>() - std::declval<__type3>())) __type38;
    typedef decltype(std::declval<__type8>()(std::declval<__type10>(), std::declval<__type1>())) __type39;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type39>::type::iterator>::value_type>::type __type40;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type40>(), std::declval<__type16>())) __type41;
    typedef decltype(std::declval<__type13>()[std::declval<__type41>()]) __type42;
    typedef decltype((pythonic::operator_::add(std::declval<__type12>(), std::declval<__type42>()))) __type43;
    typedef decltype((std::declval<__type43>() - std::declval<__type3>())) __type44;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type38>(), std::declval<__type44>())) __type45;
    typedef indexable<__type45> __type46;
    typedef typename __combined<__type34,__type46>::type __type47;
    typedef typename __combined<__type47,__type46>::type __type48;
    typedef decltype((pythonic::operator_::add(std::declval<__type12>(), std::declval<__type4>()))) __type49;
    typedef typename pythonic::lazy<__type49>::type __type50;
    typedef typename __combined<__type12,__type50>::type __type51;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::maximum{})>::type>::type __type52;
    typedef typename __combined<__type47,__type30>::type __type53;
    typedef decltype(pythonic::__builtin__::getattr(pythonic::types::attr::T{}, std::declval<__type53>())) __type54;
    typedef typename pythonic::assignable<decltype(std::declval<__type52>()(std::declval<__type53>(), std::declval<__type54>()))>::type __type55;
    typedef decltype((pythonic::operator_::div(std::declval<__type55>(), std::declval<__type25>()))) __type56;
    typedef typename __combined<__type55,__type56>::type __type57;
    typename pythonic::assignable<typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type39>::type::iterator>::value_type>::type>::type j;
    typename pythonic::assignable<typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type15>::type::iterator>::value_type>::type>::type k;
    typename pythonic::assignable<typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type15>::type::iterator>::value_type>::type>::type k_;
    typename pythonic::assignable<typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type9>::type::iterator>::value_type>::type>::type i;
    typename pythonic::assignable<typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type9>::type::iterator>::value_type>::type>::type i_;
    typename pythonic::assignable<decltype((q - 1L))>::type s = (q - 1L);
    typename pythonic::assignable<decltype((pythonic::operator_::mul(n_cols, s)))>::type expanded_cols = (pythonic::operator_::mul(n_cols, s));
    typename pythonic::assignable<typename __combined<__type31,__type25>::type>::type Pi = pythonic::numpy::functor::zeros{}(expanded_cols, pythonic::numpy::functor::float64{});
    typename pythonic::assignable<typename __combined<__type48,__type30>::type>::type Pij = pythonic::numpy::functor::zeros{}(pythonic::__builtin__::pythran::functor::make_shape{}(expanded_cols, expanded_cols), pythonic::numpy::functor::float64{});
    {
      for (long  i=0L; i < n_cols; i += 1L)
      {
        typename pythonic::lazy<decltype((pythonic::operator_::mul(i, s)))>::type i0 = (pythonic::operator_::mul(i, s));
        {
          for (long  k=0L; k < depth; k += 1L)
          {
            ;
            if ((pythonic::operator_::ne(alignment.fast(pythonic::types::make_tuple(i, k)), q)))
            {
              Pi[((pythonic::operator_::add(i0, alignment.fast(pythonic::types::make_tuple(i, k)))) - 1L)] += W.fast(k);
            }
          }
        }
      }
    }
    {
      for (long  i_=0L; i_ < n_cols; i_ += 1L)
      {
        ;
        typename pythonic::lazy<__type51>::type j0 = (pythonic::operator_::mul(i_, s));
        {
          for (long  j=i_; j < n_cols; j += 1L)
          {
            {
              for (long  k_=0L; k_ < depth; k_ += 1L)
              {
                ;
                ;
                if (pythonic::__builtin__::pythran::and_([&] () { return (pythonic::operator_::ne(alignment.fast(pythonic::types::make_tuple(i_, k_)), q)); }, [&] () { return (pythonic::operator_::ne(alignment.fast(pythonic::types::make_tuple(j, k_)), q)); }))
                {
                  Pij[pythonic::types::make_tuple(((pythonic::operator_::add((pythonic::operator_::mul(i_, s)), alignment.fast(pythonic::types::make_tuple(i_, k_)))) - 1L), ((pythonic::operator_::add(j0, alignment.fast(pythonic::types::make_tuple(j, k_)))) - 1L))] += W.fast(k_);
                }
              }
            }
            j0 = (pythonic::operator_::add(j0, s));
          }
        }
      }
    }
    typename pythonic::assignable<decltype(pythonic::numpy::functor::sum{}(W))>::type Meff = pythonic::numpy::functor::sum{}(W);
    pythonic::operator_::idiv(Pi, Meff);
    typename pythonic::assignable<typename __combined<__type57,__type25>::type>::type Pij_ = pythonic::numpy::functor::maximum{}(Pij, pythonic::__builtin__::getattr(pythonic::types::attr::T{}, Pij));
    pythonic::operator_::idiv(Pij_, Meff);
    return pythonic::types::make_tuple(Pi, Pij_);
  }
  template <typename argument_type0 , typename argument_type1 , typename argument_type2 , typename argument_type3 >
  typename _compute_weights::type<argument_type0, argument_type1, argument_type2, argument_type3>::result_type _compute_weights::operator()(argument_type0&& alignment, argument_type1&& theta, argument_type2&& n_cols, argument_type3&& depth) const
  {
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::ones{})>::type>::type __type0;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type3>::type>::type __type1;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::float64{})>::type>::type __type2;
    typedef typename pythonic::assignable<decltype(std::declval<__type0>()(std::declval<__type1>(), std::declval<__type2>()))>::type __type3;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::range{})>::type>::type __type4;
    typedef long __type5;
    typedef decltype((std::declval<__type1>() - std::declval<__type5>())) __type6;
    typedef decltype(std::declval<__type4>()(std::declval<__type6>())) __type7;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type7>::type::iterator>::value_type>::type __type8;
    typedef indexable<__type8> __type9;
    typedef typename __combined<__type3,__type9>::type __type10;
    typedef decltype((pythonic::operator_::add(std::declval<__type8>(), std::declval<__type5>()))) __type11;
    typedef decltype(std::declval<__type4>()(std::declval<__type11>(), std::declval<__type1>())) __type12;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type12>::type::iterator>::value_type>::type __type13;
    typedef indexable<__type13> __type14;
    typedef typename __combined<__type10,__type14>::type __type15;
    typedef typename __combined<__type15,__type9>::type __type16;
    typedef double __type17;
    typedef container<typename std::remove_reference<__type17>::type> __type18;
    typedef typename __combined<__type16,__type18>::type __type19;
    typedef typename __combined<__type19,__type14>::type __type20;
    typedef typename __combined<__type20,__type18>::type __type21;
    typename pythonic::assignable<typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type12>::type::iterator>::value_type>::type>::type j;
    typename pythonic::assignable<typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type7>::type::iterator>::value_type>::type>::type i;
    typename pythonic::assignable<decltype(pythonic::numpy::functor::floor{}((pythonic::operator_::mul(theta, n_cols))))>::type _thresh = pythonic::numpy::functor::floor{}((pythonic::operator_::mul(theta, n_cols)));
    typename pythonic::assignable<typename __combined<__type19,__type14>::type>::type counts = pythonic::numpy::functor::ones{}(depth, pythonic::numpy::functor::float64{});
    if ((pythonic::operator_::eq(theta, 0L)))
    {
      ;
      return pythonic::types::make_tuple(depth, counts);
    }
    {
      #pragma omp parallel for schedule(dynamic, 10)
      for (long  i=0L; i < (depth - 1L); i += 1L)
      {
        typename pythonic::assignable<decltype(alignment(i,pythonic::types::contiguous_slice(pythonic::__builtin__::None,pythonic::__builtin__::None)))>::type this_vec = alignment(i,pythonic::types::contiguous_slice(pythonic::__builtin__::None,pythonic::__builtin__::None));
        {
          for (long  j=(pythonic::operator_::add(i, 1L)); j < depth; j += 1L)
          {
            ;
            if ((pythonic::operator_::lt(pythonic::numpy::functor::sum{}((pythonic::operator_::ne(this_vec, alignment(j,pythonic::types::contiguous_slice(pythonic::__builtin__::None,pythonic::__builtin__::None))))), _thresh)))
            {
              counts.fast(i) += 1.0;
              counts.fast(j) += 1.0;
            }
          }
        }
      }
    }
    typename pythonic::assignable<typename pythonic::assignable<decltype((pythonic::operator_::div(std::declval<__type17>(), std::declval<__type21>())))>::type>::type weights = (pythonic::operator_::div(1.0, counts));
    ;
    return pythonic::types::make_tuple(pythonic::numpy::functor::sum{}(weights), weights);
  }
  template <typename argument_type0 >
  typename _compute_theta::type<argument_type0>::result_type _compute_theta::operator()(argument_type0&& alignment) const
  {
    typedef typename pythonic::assignable<double>::type __type0;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::sum{})>::type>::type __type1;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::bincount{})>::type>::type __type2;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type3;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::range{})>::type>::type __type4;
    typedef decltype(pythonic::__builtin__::getattr(pythonic::types::attr::SHAPE{}, std::declval<__type3>())) __type5;
    typedef typename std::tuple_element<0,typename std::remove_reference<__type5>::type>::type __type6;
    typedef decltype(std::declval<__type4>()(std::declval<__type6>())) __type7;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type7>::type::iterator>::value_type>::type __type8;
    typedef pythonic::types::contiguous_slice __type9;
    typedef decltype(std::declval<__type3>()(std::declval<__type8>(), std::declval<__type9>())) __type10;
    typedef typename pythonic::assignable<decltype(std::declval<__type2>()(std::declval<__type10>()))>::type __type11;
    typedef long __type12;
    typedef decltype((std::declval<__type11>() - std::declval<__type12>())) __type13;
    typedef decltype((pythonic::operator_::mul(std::declval<__type11>(), std::declval<__type13>()))) __type14;
    typedef decltype((pythonic::operator_::div(std::declval<__type14>(), std::declval<__type12>()))) __type15;
    typedef decltype(std::declval<__type1>()(std::declval<__type15>())) __type16;
    typedef decltype((pythonic::operator_::add(std::declval<__type0>(), std::declval<__type16>()))) __type17;
    typedef typename __combined<__type0,__type17>::type __type18;
    typedef double __type19;
    typedef typename pythonic::assignable<typename std::tuple_element<1,typename std::remove_reference<__type5>::type>::type>::type __type20;
    typedef decltype((pythonic::operator_::mul(std::declval<__type19>(), std::declval<__type20>()))) __type21;
    typedef decltype((std::declval<__type20>() - std::declval<__type12>())) __type22;
    typedef decltype((pythonic::operator_::mul(std::declval<__type21>(), std::declval<__type22>()))) __type23;
    typedef decltype((pythonic::operator_::mul(std::declval<__type23>(), std::declval<__type6>()))) __type24;
    typedef decltype((pythonic::operator_::div(std::declval<__type18>(), std::declval<__type24>()))) __type25;
    typedef typename __combined<__type18,__type25>::type __type26;
    typedef typename __combined<__type26,__type16>::type __type27;
    typename pythonic::assignable<typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type7>::type::iterator>::value_type>::type>::type i;
    typename pythonic::assignable<decltype(std::get<1>(pythonic::__builtin__::getattr(pythonic::types::attr::SHAPE{}, alignment)))>::type alignment_depth = std::get<1>(pythonic::__builtin__::getattr(pythonic::types::attr::SHAPE{}, alignment));
    ;
    typename pythonic::assignable<typename __combined<__type27,__type24>::type>::type meanfracid = 0.0;
    {
      long  __target140301692805920 = std::get<0>(pythonic::__builtin__::getattr(pythonic::types::attr::SHAPE{}, alignment));
      for (long  i=0L; i < __target140301692805920; i += 1L)
      {
        typename pythonic::assignable<decltype(pythonic::numpy::functor::bincount{}(alignment(i,pythonic::types::contiguous_slice(pythonic::__builtin__::None,pythonic::__builtin__::None))))>::type match_groups = pythonic::numpy::functor::bincount{}(alignment(i,pythonic::types::contiguous_slice(pythonic::__builtin__::None,pythonic::__builtin__::None)));
        meanfracid += pythonic::numpy::functor::sum{}((pythonic::operator_::div((pythonic::operator_::mul(match_groups, (match_groups - 1L))), 2L)));
      }
    }
    pythonic::operator_::idiv(meanfracid, (pythonic::operator_::mul((pythonic::operator_::mul((pythonic::operator_::mul(0.5, alignment_depth)), (alignment_depth - 1L))), std::get<0>(pythonic::__builtin__::getattr(pythonic::types::attr::SHAPE{}, alignment)))));
    ;
    return pythonic::__builtin__::functor::min{}(0.5, (pythonic::operator_::div(0.1216, meanfracid)));
  }
  template <typename argument_type0 >
  typename apc_correction::type<argument_type0>::result_type apc_correction::operator()(argument_type0&& matrix) const
  {
    typename pythonic::assignable<decltype((matrix - (pythonic::operator_::div((pythonic::operator_::mul(pythonic::numpy::functor::mean{}(matrix, 0L)(pythonic::__builtin__::None,pythonic::types::contiguous_slice(pythonic::__builtin__::None,pythonic::__builtin__::None)), pythonic::numpy::functor::mean{}(matrix, 1L)(pythonic::types::contiguous_slice(pythonic::__builtin__::None,pythonic::__builtin__::None),pythonic::__builtin__::None))), pythonic::numpy::functor::mean{}(matrix)))))>::type corrected = (matrix - (pythonic::operator_::div((pythonic::operator_::mul(pythonic::numpy::functor::mean{}(matrix, 0L)(pythonic::__builtin__::None,pythonic::types::contiguous_slice(pythonic::__builtin__::None,pythonic::__builtin__::None)), pythonic::numpy::functor::mean{}(matrix, 1L)(pythonic::types::contiguous_slice(pythonic::__builtin__::None,pythonic::__builtin__::None),pythonic::__builtin__::None))), pythonic::numpy::functor::mean{}(matrix))));
    pythonic::numpy::functor::fill_diagonal{}(corrected, 0.0);
    return corrected;
  }
  template <typename argument_type0 , typename argument_type1 , typename argument_type2 >
  typename compute_FN::type<argument_type0, argument_type1, argument_type2>::result_type compute_FN::operator()(argument_type0&& mJ, argument_type1&& n_cols, argument_type2&& alphabet_size) const
  {
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::zeros{})>::type>::type __type0;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::pythran::functor::make_shape{})>::type>::type __type1;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type2;
    typedef decltype(std::declval<__type1>()(std::declval<__type2>(), std::declval<__type2>())) __type3;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::float64{})>::type>::type __type4;
    typedef typename pythonic::assignable<decltype(std::declval<__type0>()(std::declval<__type3>(), std::declval<__type4>()))>::type __type5;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::range{})>::type>::type __type6;
    typedef long __type7;
    typedef decltype((std::declval<__type2>() - std::declval<__type7>())) __type8;
    typedef decltype(std::declval<__type6>()(std::declval<__type8>())) __type9;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type9>::type::iterator>::value_type>::type __type10;
    typedef decltype((pythonic::operator_::add(std::declval<__type10>(), std::declval<__type7>()))) __type11;
    typedef decltype(std::declval<__type6>()(std::declval<__type11>(), std::declval<__type2>())) __type12;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type12>::type::iterator>::value_type>::type __type13;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type10>(), std::declval<__type13>())) __type14;
    typedef indexable<__type14> __type15;
    typedef typename __combined<__type5,__type15>::type __type16;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type13>(), std::declval<__type10>())) __type17;
    typedef indexable<__type17> __type18;
    typedef typename __combined<__type16,__type18>::type __type19;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::sum{})>::type>::type __type20;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::square{})>::type>::type __type21;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type22;
    typedef pythonic::types::contiguous_slice __type23;
    typedef typename pythonic::assignable<decltype(std::declval<__type22>()(std::declval<__type23>(), std::declval<__type23>()))>::type __type24;
    typedef decltype(std::declval<__type20>()(std::declval<__type24>(), std::declval<__type7>())) __type25;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type26;
    typedef typename pythonic::assignable<typename pythonic::assignable<decltype((std::declval<__type26>() - std::declval<__type7>()))>::type>::type __type27;
    typedef decltype((pythonic::operator_::div(std::declval<__type25>(), std::declval<__type27>()))) __type28;
    typedef pythonic::types::none_type __type29;
    typedef decltype(std::declval<__type28>()(std::declval<__type23>(), std::declval<__type29>())) __type30;
    typedef decltype((std::declval<__type24>() - std::declval<__type30>())) __type31;
    typedef decltype(std::declval<__type28>()(std::declval<__type29>(), std::declval<__type23>())) __type32;
    typedef decltype((std::declval<__type31>() - std::declval<__type32>())) __type33;
    typedef decltype(std::declval<__type20>()(std::declval<__type24>())) __type34;
    typedef typename pythonic::assignable<decltype((std::declval<__type26>() - std::declval<__type7>()))>::type __type35;
    typedef typename pythonic::assignable<decltype(std::declval<__type21>()(std::declval<__type35>()))>::type __type36;
    typedef decltype((pythonic::operator_::div(std::declval<__type34>(), std::declval<__type36>()))) __type37;
    typedef decltype((pythonic::operator_::add(std::declval<__type33>(), std::declval<__type37>()))) __type38;
    typedef decltype(std::declval<__type21>()(std::declval<__type38>())) __type39;
    typedef typename pythonic::assignable<decltype(std::declval<__type20>()(std::declval<__type39>()))>::type __type40;
    typedef container<typename std::remove_reference<__type40>::type> __type41;
    typedef typename __combined<__type19,__type41>::type __type42;
    typedef typename __combined<__type42,__type15>::type __type43;
    typename pythonic::assignable<typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type12>::type::iterator>::value_type>::type>::type j;
    typename pythonic::assignable<typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type9>::type::iterator>::value_type>::type>::type i;
    typename pythonic::assignable<typename __combined<__type43,__type18>::type>::type FN = pythonic::numpy::functor::zeros{}(pythonic::__builtin__::pythran::functor::make_shape{}(n_cols, n_cols), pythonic::numpy::functor::float64{});
    typename pythonic::assignable<decltype((alphabet_size - 1L))>::type s = (alphabet_size - 1L);
    typename pythonic::assignable<decltype(s)>::type fs = s;
    typename pythonic::assignable<decltype(pythonic::numpy::functor::square{}(s))>::type fs2 = pythonic::numpy::functor::square{}(s);
    {
      for (long  i=0L; i < (n_cols - 1L); i += 1L)
      {
        typename pythonic::assignable<decltype((pythonic::operator_::mul(i, s)))>::type _row = (pythonic::operator_::mul(i, s));
        {
          for (long  j=(pythonic::operator_::add(i, 1L)); j < n_cols; j += 1L)
          {
            typename pythonic::assignable<decltype((pythonic::operator_::mul(j, s)))>::type _col = (pythonic::operator_::mul(j, s));
            typename pythonic::assignable<decltype(mJ(pythonic::types::contiguous_slice(_row,(pythonic::operator_::add(_row, s))),pythonic::types::contiguous_slice(_col,(pythonic::operator_::add(_col, s)))))>::type patch = mJ(pythonic::types::contiguous_slice(_row,(pythonic::operator_::add(_row, s))),pythonic::types::contiguous_slice(_col,(pythonic::operator_::add(_col, s))));
            ;
            ;
            ;
            ;
            typename pythonic::assignable<decltype(pythonic::numpy::functor::sum{}(pythonic::numpy::functor::square{}((pythonic::operator_::add(((patch - (pythonic::operator_::div(pythonic::numpy::functor::sum{}(patch, 1L), fs))(pythonic::types::contiguous_slice(pythonic::__builtin__::None,pythonic::__builtin__::None),pythonic::__builtin__::None)) - (pythonic::operator_::div(pythonic::numpy::functor::sum{}(patch, 0L), fs))(pythonic::__builtin__::None,pythonic::types::contiguous_slice(pythonic::__builtin__::None,pythonic::__builtin__::None))), (pythonic::operator_::div(pythonic::numpy::functor::sum{}(patch), fs2)))))))>::type fn = pythonic::numpy::functor::sum{}(pythonic::numpy::functor::square{}((pythonic::operator_::add(((patch - (pythonic::operator_::div(pythonic::numpy::functor::sum{}(patch, 1L), fs))(pythonic::types::contiguous_slice(pythonic::__builtin__::None,pythonic::__builtin__::None),pythonic::__builtin__::None)) - (pythonic::operator_::div(pythonic::numpy::functor::sum{}(patch, 0L), fs))(pythonic::__builtin__::None,pythonic::types::contiguous_slice(pythonic::__builtin__::None,pythonic::__builtin__::None))), (pythonic::operator_::div(pythonic::numpy::functor::sum{}(patch), fs2))))));
            FN.fast(pythonic::types::make_tuple(i, j)) = fn;
            FN.fast(pythonic::types::make_tuple(j, i)) = fn;
          }
        }
      }
    }
    typename pythonic::assignable<decltype(pythonic::numpy::functor::sqrt{}(FN))>::type FN_ = pythonic::numpy::functor::sqrt{}(FN);
    return pythonic::types::make_tuple(FN_, apc_correction()(FN_));
  }
  template <typename argument_type0 , typename argument_type1 , typename argument_type2 >
  typename compute_weights::type<argument_type0, argument_type1, argument_type2>::result_type compute_weights::operator()(argument_type0&& alignment, argument_type1&& alignment_T, argument_type2&& theta) const
  {
    typedef typename pythonic::assignable<typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type>::type __type0;
    typedef _compute_theta __type1;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type2;
    typedef typename pythonic::assignable<decltype(std::declval<__type1>()(std::declval<__type2>()))>::type __type3;
    typename pythonic::assignable<typename __combined<__type0,__type3>::type>::type theta_ = theta;
    if ((pythonic::operator_::le(theta_, 0.0)))
    {
      theta_ = _compute_theta()(alignment);
    }
    ;
    ;
    ;
    ;
    ;
    return std::get<1>(_compute_weights()(alignment_T, theta_, std::get<1>(pythonic::__builtin__::getattr(pythonic::types::attr::SHAPE{}, alignment_T)), std::get<0>(pythonic::__builtin__::getattr(pythonic::types::attr::SHAPE{}, alignment_T))));
  }
  template <typename argument_type0 , typename argument_type1 , typename argument_type2 >
  typename _compute_covar::type<argument_type0, argument_type1, argument_type2>::result_type _compute_covar::operator()(argument_type0&& alignment, argument_type1&& weights, argument_type2&& pseudocount) const
  {
    ;
    typename pythonic::assignable<decltype(std::get<0>(pythonic::__builtin__::getattr(pythonic::types::attr::SHAPE{}, alignment)))>::type n_cols = std::get<0>(pythonic::__builtin__::getattr(pythonic::types::attr::SHAPE{}, alignment));
    typename pythonic::assignable<decltype(pythonic::numpy::functor::max{}(alignment))>::type alphabet_size = pythonic::numpy::functor::max{}(alignment);
    typename pythonic::assignable<decltype(_compute_freqs()(alignment, n_cols, std::get<1>(pythonic::__builtin__::getattr(pythonic::types::attr::SHAPE{}, alignment)), alphabet_size, weights))>::type __tuple0 = _compute_freqs()(alignment, n_cols, std::get<1>(pythonic::__builtin__::getattr(pythonic::types::attr::SHAPE{}, alignment)), alphabet_size, weights);
    ;
    ;
    typename pythonic::assignable<decltype(_add_pseudocount()(std::get<0>(__tuple0), std::get<1>(__tuple0), pseudocount, n_cols, alphabet_size))>::type __tuple1 = _add_pseudocount()(std::get<0>(__tuple0), std::get<1>(__tuple0), pseudocount, n_cols, alphabet_size);
    ;
    ;
    typename pythonic::assignable<decltype(std::get<0>(__tuple1)(pythonic::types::contiguous_slice(pythonic::__builtin__::None,pythonic::__builtin__::None),pythonic::__builtin__::None))>::type Pi_np = std::get<0>(__tuple1)(pythonic::types::contiguous_slice(pythonic::__builtin__::None,pythonic::__builtin__::None),pythonic::__builtin__::None);
    ;
    return (std::get<1>(__tuple1) - (pythonic::operator_::mul(Pi_np, pythonic::__builtin__::getattr(pythonic::types::attr::T{}, Pi_np))));
  }
  template <typename argument_type0 , typename argument_type1 , typename argument_type2 >
  typename prepare_covariance::type<argument_type0, argument_type1, argument_type2>::result_type prepare_covariance::operator()(argument_type0&& alignment, argument_type1&& alignment_T, argument_type2 pseudocount) const
  {
    ;
    ;
    ;
    typename pythonic::assignable<decltype(_compute_weights()(alignment_T, _compute_theta()(alignment), std::get<1>(pythonic::__builtin__::getattr(pythonic::types::attr::SHAPE{}, alignment_T)), std::get<0>(pythonic::__builtin__::getattr(pythonic::types::attr::SHAPE{}, alignment_T))))>::type __tuple0 = _compute_weights()(alignment_T, _compute_theta()(alignment), std::get<1>(pythonic::__builtin__::getattr(pythonic::types::attr::SHAPE{}, alignment_T)), std::get<0>(pythonic::__builtin__::getattr(pythonic::types::attr::SHAPE{}, alignment_T)));
    ;
    ;
    ;
    return pythonic::types::make_tuple(_compute_covar()(alignment, std::get<1>(__tuple0), pseudocount), std::get<0>(__tuple0));
  }
}
#include <pythonic/python/exception_handler.hpp>
#ifdef ENABLE_PYTHON_MODULE
typename __pythran__gdca::compute_FN::type<pythonic::types::numpy_gexpr<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>,pythonic::types::normalized_slice, pythonic::types::normalized_slice>, long, int8_t>::result_type compute_FN0(pythonic::types::numpy_gexpr<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>,pythonic::types::normalized_slice, pythonic::types::normalized_slice>&& mJ, long&& n_cols, int8_t&& alphabet_size) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran__gdca::compute_FN()(mJ, n_cols, alphabet_size);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran__gdca::compute_FN::type<pythonic::types::numpy_gexpr<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>,pythonic::types::normalized_slice, pythonic::types::normalized_slice>, long, int8_t>::result_type compute_FN1(pythonic::types::numpy_gexpr<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>,pythonic::types::normalized_slice, pythonic::types::normalized_slice>&& mJ, long&& n_cols, int8_t&& alphabet_size) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran__gdca::compute_FN()(mJ, n_cols, alphabet_size);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran__gdca::compute_FN::type<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>, long, int8_t>::result_type compute_FN2(pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>&& mJ, long&& n_cols, int8_t&& alphabet_size) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran__gdca::compute_FN()(mJ, n_cols, alphabet_size);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran__gdca::compute_FN::type<pythonic::types::numpy_texpr<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>>, long, int8_t>::result_type compute_FN3(pythonic::types::numpy_texpr<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>>&& mJ, long&& n_cols, int8_t&& alphabet_size) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran__gdca::compute_FN()(mJ, n_cols, alphabet_size);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran__gdca::compute_FN::type<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>, long, int8_t>::result_type compute_FN4(pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>&& mJ, long&& n_cols, int8_t&& alphabet_size) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran__gdca::compute_FN()(mJ, n_cols, alphabet_size);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran__gdca::compute_FN::type<pythonic::types::numpy_texpr<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>>, long, int8_t>::result_type compute_FN5(pythonic::types::numpy_texpr<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>>&& mJ, long&& n_cols, int8_t&& alphabet_size) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran__gdca::compute_FN()(mJ, n_cols, alphabet_size);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran__gdca::compute_weights::type<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>, pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>, double>::result_type compute_weights0(pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>&& alignment, pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>&& alignment_T, double&& theta) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran__gdca::compute_weights()(alignment, alignment_T, theta);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran__gdca::compute_weights::type<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>, pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>, double>::result_type compute_weights1(pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>&& alignment, pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>&& alignment_T, double&& theta) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran__gdca::compute_weights()(alignment, alignment_T, theta);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran__gdca::compute_weights::type<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>, pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>, double>::result_type compute_weights2(pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>&& alignment, pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>&& alignment_T, double&& theta) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran__gdca::compute_weights()(alignment, alignment_T, theta);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran__gdca::compute_weights::type<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>, pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>, double>::result_type compute_weights3(pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>&& alignment, pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>&& alignment_T, double&& theta) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran__gdca::compute_weights()(alignment, alignment_T, theta);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran__gdca::prepare_covariance::type<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>, pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>::result_type prepare_covariance0(pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>&& alignment, pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>&& alignment_T) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran__gdca::prepare_covariance()(alignment, alignment_T);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran__gdca::prepare_covariance::type<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>, pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>::result_type prepare_covariance1(pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>&& alignment, pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>&& alignment_T) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran__gdca::prepare_covariance()(alignment, alignment_T);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran__gdca::prepare_covariance::type<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>, pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>::result_type prepare_covariance2(pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>&& alignment, pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>&& alignment_T) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran__gdca::prepare_covariance()(alignment, alignment_T);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran__gdca::prepare_covariance::type<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>, pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>::result_type prepare_covariance3(pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>&& alignment, pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>&& alignment_T) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran__gdca::prepare_covariance()(alignment, alignment_T);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran__gdca::prepare_covariance::type<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>, pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>, double>::result_type prepare_covariance4(pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>&& alignment, pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>&& alignment_T, double&& pseudocount) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran__gdca::prepare_covariance()(alignment, alignment_T, pseudocount);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran__gdca::prepare_covariance::type<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>, pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>, double>::result_type prepare_covariance5(pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>&& alignment, pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>&& alignment_T, double&& pseudocount) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran__gdca::prepare_covariance()(alignment, alignment_T, pseudocount);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran__gdca::prepare_covariance::type<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>, pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>, double>::result_type prepare_covariance6(pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>&& alignment, pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>&& alignment_T, double&& pseudocount) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran__gdca::prepare_covariance()(alignment, alignment_T, pseudocount);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran__gdca::prepare_covariance::type<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>, pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>, double>::result_type prepare_covariance7(pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>&& alignment, pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>&& alignment_T, double&& pseudocount) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran__gdca::prepare_covariance()(alignment, alignment_T, pseudocount);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran__gdca::apc_correction::type<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>>::result_type apc_correction0(pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>&& matrix) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran__gdca::apc_correction()(matrix);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran__gdca::apc_correction::type<pythonic::types::numpy_texpr<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>>>::result_type apc_correction1(pythonic::types::numpy_texpr<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>>&& matrix) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran__gdca::apc_correction()(matrix);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}

static PyObject *
__pythran_wrap_compute_FN0(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[3+1];
    char const* keywords[] = {"mJ","n_cols","alphabet_size", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOO",
                                     (char**)keywords, &args_obj[0], &args_obj[1], &args_obj[2]))
        return nullptr;
    if(is_convertible<pythonic::types::numpy_gexpr<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>,pythonic::types::normalized_slice, pythonic::types::normalized_slice>>(args_obj[0]) && is_convertible<long>(args_obj[1]) && is_convertible<int8_t>(args_obj[2]))
        return to_python(compute_FN0(from_python<pythonic::types::numpy_gexpr<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>,pythonic::types::normalized_slice, pythonic::types::normalized_slice>>(args_obj[0]), from_python<long>(args_obj[1]), from_python<int8_t>(args_obj[2])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_compute_FN1(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[3+1];
    char const* keywords[] = {"mJ","n_cols","alphabet_size", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOO",
                                     (char**)keywords, &args_obj[0], &args_obj[1], &args_obj[2]))
        return nullptr;
    if(is_convertible<pythonic::types::numpy_gexpr<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>,pythonic::types::normalized_slice, pythonic::types::normalized_slice>>(args_obj[0]) && is_convertible<long>(args_obj[1]) && is_convertible<int8_t>(args_obj[2]))
        return to_python(compute_FN1(from_python<pythonic::types::numpy_gexpr<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>,pythonic::types::normalized_slice, pythonic::types::normalized_slice>>(args_obj[0]), from_python<long>(args_obj[1]), from_python<int8_t>(args_obj[2])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_compute_FN2(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[3+1];
    char const* keywords[] = {"mJ","n_cols","alphabet_size", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOO",
                                     (char**)keywords, &args_obj[0], &args_obj[1], &args_obj[2]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>>(args_obj[0]) && is_convertible<long>(args_obj[1]) && is_convertible<int8_t>(args_obj[2]))
        return to_python(compute_FN2(from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>>(args_obj[0]), from_python<long>(args_obj[1]), from_python<int8_t>(args_obj[2])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_compute_FN3(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[3+1];
    char const* keywords[] = {"mJ","n_cols","alphabet_size", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOO",
                                     (char**)keywords, &args_obj[0], &args_obj[1], &args_obj[2]))
        return nullptr;
    if(is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>>>(args_obj[0]) && is_convertible<long>(args_obj[1]) && is_convertible<int8_t>(args_obj[2]))
        return to_python(compute_FN3(from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>>>(args_obj[0]), from_python<long>(args_obj[1]), from_python<int8_t>(args_obj[2])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_compute_FN4(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[3+1];
    char const* keywords[] = {"mJ","n_cols","alphabet_size", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOO",
                                     (char**)keywords, &args_obj[0], &args_obj[1], &args_obj[2]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>>(args_obj[0]) && is_convertible<long>(args_obj[1]) && is_convertible<int8_t>(args_obj[2]))
        return to_python(compute_FN4(from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>>(args_obj[0]), from_python<long>(args_obj[1]), from_python<int8_t>(args_obj[2])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_compute_FN5(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[3+1];
    char const* keywords[] = {"mJ","n_cols","alphabet_size", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOO",
                                     (char**)keywords, &args_obj[0], &args_obj[1], &args_obj[2]))
        return nullptr;
    if(is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>>>(args_obj[0]) && is_convertible<long>(args_obj[1]) && is_convertible<int8_t>(args_obj[2]))
        return to_python(compute_FN5(from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>>>(args_obj[0]), from_python<long>(args_obj[1]), from_python<int8_t>(args_obj[2])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_compute_weights0(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[3+1];
    char const* keywords[] = {"alignment","alignment_T","theta", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOO",
                                     (char**)keywords, &args_obj[0], &args_obj[1], &args_obj[2]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[1]) && is_convertible<double>(args_obj[2]))
        return to_python(compute_weights0(from_python<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[0]), from_python<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[1]), from_python<double>(args_obj[2])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_compute_weights1(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[3+1];
    char const* keywords[] = {"alignment","alignment_T","theta", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOO",
                                     (char**)keywords, &args_obj[0], &args_obj[1], &args_obj[2]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[0]) && is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[1]) && is_convertible<double>(args_obj[2]))
        return to_python(compute_weights1(from_python<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[0]), from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[1]), from_python<double>(args_obj[2])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_compute_weights2(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[3+1];
    char const* keywords[] = {"alignment","alignment_T","theta", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOO",
                                     (char**)keywords, &args_obj[0], &args_obj[1], &args_obj[2]))
        return nullptr;
    if(is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[1]) && is_convertible<double>(args_obj[2]))
        return to_python(compute_weights2(from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[0]), from_python<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[1]), from_python<double>(args_obj[2])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_compute_weights3(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[3+1];
    char const* keywords[] = {"alignment","alignment_T","theta", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOO",
                                     (char**)keywords, &args_obj[0], &args_obj[1], &args_obj[2]))
        return nullptr;
    if(is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[0]) && is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[1]) && is_convertible<double>(args_obj[2]))
        return to_python(compute_weights3(from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[0]), from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[1]), from_python<double>(args_obj[2])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_prepare_covariance0(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[2+1];
    char const* keywords[] = {"alignment","alignment_T", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OO",
                                     (char**)keywords, &args_obj[0], &args_obj[1]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[1]))
        return to_python(prepare_covariance0(from_python<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[0]), from_python<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[1])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_prepare_covariance1(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[2+1];
    char const* keywords[] = {"alignment","alignment_T", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OO",
                                     (char**)keywords, &args_obj[0], &args_obj[1]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[0]) && is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[1]))
        return to_python(prepare_covariance1(from_python<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[0]), from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[1])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_prepare_covariance2(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[2+1];
    char const* keywords[] = {"alignment","alignment_T", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OO",
                                     (char**)keywords, &args_obj[0], &args_obj[1]))
        return nullptr;
    if(is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[1]))
        return to_python(prepare_covariance2(from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[0]), from_python<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[1])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_prepare_covariance3(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[2+1];
    char const* keywords[] = {"alignment","alignment_T", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OO",
                                     (char**)keywords, &args_obj[0], &args_obj[1]))
        return nullptr;
    if(is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[0]) && is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[1]))
        return to_python(prepare_covariance3(from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[0]), from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[1])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_prepare_covariance4(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[3+1];
    char const* keywords[] = {"alignment","alignment_T","pseudocount", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOO",
                                     (char**)keywords, &args_obj[0], &args_obj[1], &args_obj[2]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[1]) && is_convertible<double>(args_obj[2]))
        return to_python(prepare_covariance4(from_python<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[0]), from_python<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[1]), from_python<double>(args_obj[2])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_prepare_covariance5(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[3+1];
    char const* keywords[] = {"alignment","alignment_T","pseudocount", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOO",
                                     (char**)keywords, &args_obj[0], &args_obj[1], &args_obj[2]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[0]) && is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[1]) && is_convertible<double>(args_obj[2]))
        return to_python(prepare_covariance5(from_python<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[0]), from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[1]), from_python<double>(args_obj[2])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_prepare_covariance6(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[3+1];
    char const* keywords[] = {"alignment","alignment_T","pseudocount", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOO",
                                     (char**)keywords, &args_obj[0], &args_obj[1], &args_obj[2]))
        return nullptr;
    if(is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[1]) && is_convertible<double>(args_obj[2]))
        return to_python(prepare_covariance6(from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[0]), from_python<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>(args_obj[1]), from_python<double>(args_obj[2])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_prepare_covariance7(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[3+1];
    char const* keywords[] = {"alignment","alignment_T","pseudocount", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOO",
                                     (char**)keywords, &args_obj[0], &args_obj[1], &args_obj[2]))
        return nullptr;
    if(is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[0]) && is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[1]) && is_convertible<double>(args_obj[2]))
        return to_python(prepare_covariance7(from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[0]), from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<int8_t,pythonic::types::pshape<long,long>>>>(args_obj[1]), from_python<double>(args_obj[2])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_apc_correction0(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[1+1];
    char const* keywords[] = {"matrix", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "O",
                                     (char**)keywords, &args_obj[0]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>>(args_obj[0]))
        return to_python(apc_correction0(from_python<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>>(args_obj[0])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_apc_correction1(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[1+1];
    char const* keywords[] = {"matrix", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "O",
                                     (char**)keywords, &args_obj[0]))
        return nullptr;
    if(is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>>>(args_obj[0]))
        return to_python(apc_correction1(from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<double,pythonic::types::pshape<long,long>>>>(args_obj[0])));
    else {
        return nullptr;
    }
}

            static PyObject *
            __pythran_wrapall_compute_FN(PyObject *self, PyObject *args, PyObject *kw)
            {
                return pythonic::handle_python_exception([self, args, kw]()
                -> PyObject* {

if(PyObject* obj = __pythran_wrap_compute_FN0(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_compute_FN1(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_compute_FN2(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_compute_FN3(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_compute_FN4(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_compute_FN5(self, args, kw))
    return obj;
PyErr_Clear();

                return pythonic::python::raise_invalid_argument(
                               "compute_FN", "\n    - compute_FN(float[::,::], int, int8)\n    - compute_FN(float64[::,::], int, int8)\n    - compute_FN(float[:,:], int, int8)\n    - compute_FN(float64[:,:], int, int8)", args, kw);
                });
            }


            static PyObject *
            __pythran_wrapall_compute_weights(PyObject *self, PyObject *args, PyObject *kw)
            {
                return pythonic::handle_python_exception([self, args, kw]()
                -> PyObject* {

if(PyObject* obj = __pythran_wrap_compute_weights0(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_compute_weights1(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_compute_weights2(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_compute_weights3(self, args, kw))
    return obj;
PyErr_Clear();

                return pythonic::python::raise_invalid_argument(
                               "compute_weights", "\n    - compute_weights(int8[:,:], int8[:,:], float)", args, kw);
                });
            }


            static PyObject *
            __pythran_wrapall_prepare_covariance(PyObject *self, PyObject *args, PyObject *kw)
            {
                return pythonic::handle_python_exception([self, args, kw]()
                -> PyObject* {

if(PyObject* obj = __pythran_wrap_prepare_covariance0(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_prepare_covariance1(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_prepare_covariance2(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_prepare_covariance3(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_prepare_covariance4(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_prepare_covariance5(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_prepare_covariance6(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_prepare_covariance7(self, args, kw))
    return obj;
PyErr_Clear();

                return pythonic::python::raise_invalid_argument(
                               "prepare_covariance", "\n    - prepare_covariance(int8[:,:], int8[:,:])\n    - prepare_covariance(int8[:,:], int8[:,:], float)", args, kw);
                });
            }


            static PyObject *
            __pythran_wrapall_apc_correction(PyObject *self, PyObject *args, PyObject *kw)
            {
                return pythonic::handle_python_exception([self, args, kw]()
                -> PyObject* {

if(PyObject* obj = __pythran_wrap_apc_correction0(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_apc_correction1(self, args, kw))
    return obj;
PyErr_Clear();

                return pythonic::python::raise_invalid_argument(
                               "apc_correction", "\n    - apc_correction(float[:,:])", args, kw);
                });
            }


static PyMethodDef Methods[] = {
    {
    "compute_FN",
    (PyCFunction)__pythran_wrapall_compute_FN,
    METH_VARARGS | METH_KEYWORDS,
    "Supported prototypes:\n\n    - compute_FN(float[::,::], int, int8)\n    - compute_FN(float64[::,::], int, int8)\n    - compute_FN(float[:,:], int, int8)\n    - compute_FN(float64[:,:], int, int8)"},{
    "compute_weights",
    (PyCFunction)__pythran_wrapall_compute_weights,
    METH_VARARGS | METH_KEYWORDS,
    "Supported prototypes:\n\n    - compute_weights(int8[:,:], int8[:,:], float)"},{
    "prepare_covariance",
    (PyCFunction)__pythran_wrapall_prepare_covariance,
    METH_VARARGS | METH_KEYWORDS,
    "Supported prototypes:\n\n    - prepare_covariance(int8[:,:], int8[:,:])\n    - prepare_covariance(int8[:,:], int8[:,:], float)"},{
    "apc_correction",
    (PyCFunction)__pythran_wrapall_apc_correction,
    METH_VARARGS | METH_KEYWORDS,
    "Supported prototypes:\n\n    - apc_correction(float[:,:])"},
    {NULL, NULL, 0, NULL}
};


#if PY_MAJOR_VERSION >= 3
  static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "_gdca",            /* m_name */
    "",         /* m_doc */
    -1,                  /* m_size */
    Methods,             /* m_methods */
    NULL,                /* m_reload */
    NULL,                /* m_traverse */
    NULL,                /* m_clear */
    NULL,                /* m_free */
  };
#define PYTHRAN_RETURN return theModule
#define PYTHRAN_MODULE_INIT(s) PyInit_##s
#else
#define PYTHRAN_RETURN return
#define PYTHRAN_MODULE_INIT(s) init##s
#endif
PyMODINIT_FUNC
PYTHRAN_MODULE_INIT(_gdca)(void)
#ifndef _WIN32
__attribute__ ((visibility("default")))
__attribute__ ((externally_visible))
#endif
;
PyMODINIT_FUNC
PYTHRAN_MODULE_INIT(_gdca)(void) {
    import_array()
    #if PY_MAJOR_VERSION >= 3
    PyObject* theModule = PyModule_Create(&moduledef);
    #else
    PyObject* theModule = Py_InitModule3("_gdca",
                                         Methods,
                                         ""
    );
    #endif
    if(! theModule)
        PYTHRAN_RETURN;
    PyObject * theDoc = Py_BuildValue("(sss)",
                                      "0.9.2",
                                      "2019-07-02 11:53:06.139307",
                                      "841f5eefc28d753e9f580a7da34751569d302d4884c41bb46f62796c3af97d24");
    if(! theDoc)
        PYTHRAN_RETURN;
    PyModule_AddObject(theModule,
                       "__pythran__",
                       theDoc);


    PYTHRAN_RETURN;
}

#endif